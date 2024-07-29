use std::{cell::RefCell, collections::BTreeMap, rc::Rc};
use std::cell::Ref;

use pyo3::{pyfunction, types::PyDict, FromPyObject, IntoPy, PyAny, PyObject, PyResult, Python};

type PythonInstanceRef = Rc<RefCell<PythonInstance>>;

#[derive(Clone, Debug)]
pub struct PythonInstance {
    id: u32,
    parent_id: Option<u32>,
    dict: PyObject,
    children: Vec<PythonInstanceRef>,
    related_objects: BTreeMap<String, Vec<PyObject>>,
}

#[derive(Clone, Debug, FromPyObject)]
pub struct Prefetch {
    group_key: String,
    fk_key: String,
    instances: Vec<PyObject>,
}

struct Parent {
    id: u32,
    name: String,
}

pub struct TreeObject {
    instances: Vec<PythonInstance>,
}

impl<'source> FromPyObject<'source> for TreeObject {
    fn extract(obj: &'source PyAny) -> PyResult<TreeObject> {
        let parent_key: Option<String> = obj
            .getattr("parent_key")
            .expect("Could not get parent key from python object")
            .extract()
            .expect("Could not get PyResult");
        let pk_key: String = obj
            .getattr("pk_key")
            .expect("Could not_get pk key from python object")
            .extract()
            .expect("Could not get String from PyResult");
        let mut instances = Vec::new();
        let py_instances: Vec<PyObject> = obj
            .getattr("instances")
            .expect("Could not unwrap PyAny")
            .extract()
            .expect("Could not cast PyResult to Vec<PyObject>");
        for py_instance in py_instances {
            let py_dict = py_instance.downcast::<PyDict>(obj.py())
                .expect("Could not downcast to PyDict");
            let id = py_dict
                .get_item(&pk_key)
                .expect("Could not retrieve PyAny")
                .expect("Option was not provided")
                .extract()
                .expect("Could not extract PyResult");
            let mut parent_id = None;
            if let Some(parent_id_from_py) = py_dict
                .get_item(&parent_key)
                .expect("Could not get element from python dict")
            {
                parent_id = parent_id_from_py
                    .extract()
                    .expect("Could not parse parent id value as u32");
            }
            instances.push(PythonInstance {
                id,
                dict: py_instance,
                parent_id,
                related_objects: BTreeMap::new(),
                children: Vec::new(),
            });
        }
        Ok(TreeObject { instances })
    }
}

impl IntoPy<PyObject> for Parent {
    fn into_py(self, py: Python) -> PyObject {
        let dict = PyDict::new(py);
        dict.set_item("name", self.name)
            .expect("Could not set name for parent");
        dict.set_item("id", self.id)
            .expect("Could not set id for parent");
        dict.into()
    }
}

impl IntoPy<PyObject> for PythonInstance {
    fn into_py(self, py: Python) -> PyObject {
        let dict = self.dict.downcast::<PyDict>(py)
            .expect("Could not downcast PyDict");
        let children: Vec<PyObject> = self
            .children
            .iter()
            .map(|elem| elem.borrow().clone().into_py(py))
            .collect();
        dict.set_item("children", children).expect("Could not set key");
        for (key, value) in self.related_objects {
            dict.set_item(key, value).expect("Could not set key")
        }
        dict.into()
    }
}

#[pyfunction]
pub fn serialize_tree(
    py: Python,
    data_set_object: TreeObject,
    prefetch_objects: Vec<Prefetch>,
    is_tree: bool,
) -> Vec<PythonInstance> {
    let mut dict_map = BTreeMap::new();
    let mut root_refs: Vec<PythonInstanceRef> = Vec::new();
    for mut dict in data_set_object.instances {
        for prefetch_object in &prefetch_objects {
            dict.related_objects.insert(prefetch_object.group_key.clone(), vec![]);
        }
        dict_map.insert(dict.id, Rc::new(RefCell::new(dict)));
    }
    add_related_objects(py, prefetch_objects, &mut dict_map);
    if !is_tree {
        return dict_map.values().map(|obj| obj.borrow().clone()).collect();
    }
    for dict in dict_map.values() {
        let borrowed_dict = dict.borrow();

        if let Some(parent_id) = borrowed_dict.parent_id {
            if let Some(parent) = dict_map.get(&parent_id) {
                map_parent(parent, parent_id, dict, borrowed_dict, py)
            }
        } else {
            root_refs.push(Rc::clone(dict))
        }
    }
    root_refs.iter().map(|root| root.borrow().clone()).collect()
}

fn map_parent(
    parent: &Rc<RefCell<PythonInstance>>,
    parent_id: u32,
    dict: &Rc<RefCell<PythonInstance>>,
    borrowed_dict: Ref<PythonInstance>,
    py: Python,
) {
    let py_dict = borrowed_dict
        .dict
        .downcast::<PyDict>(py)
        .expect("Could not downcast PyObject to PyDict");
    let mut borrowed_parent = parent.borrow_mut();
    borrowed_parent.children.push(Rc::clone(dict));
    let name: String = borrowed_parent
        .dict
        .downcast::<PyDict>(py)
        .expect("Could not cast PyAny to PyDict")
        .get_item("name")
        .expect("name was not found in PyDict")
        .expect("unwrapping to PyAny failed")
        .extract()
        .expect("Could not extract String from PyObject");
    py_dict.set_item(
        "parent",
        Parent {
            id: parent_id,
            name,
        }.into_py(py),
    ).expect("Could not set item in dict");
}

fn add_related_objects(
    py: Python,
    prefetch_objects: Vec<Prefetch>,
    dict_map: &mut BTreeMap<u32, PythonInstanceRef>,
) {
    for prefetch_object in prefetch_objects {
        for instance in prefetch_object.instances {
            let related_dict = instance
                .downcast::<PyDict>(py)
                .expect("Could not cast PyObject to PyDict");
            let fk: u32 = related_dict
                .get_item(&prefetch_object.fk_key)
                .expect("Could not find fk by provided key from dict")
                .expect("fk was not found")
                .extract()
                .expect("Could not convert PyObject to u32");
            let relation_map = &mut dict_map.get_mut(&fk).expect("Could not get map").borrow_mut().related_objects;
            if let Some(related_objects) = relation_map.get_mut(&prefetch_object.group_key) {
                related_objects.push(instance);
            }
        }
    }
}
