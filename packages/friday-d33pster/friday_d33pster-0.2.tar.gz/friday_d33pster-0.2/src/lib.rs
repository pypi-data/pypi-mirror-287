// ------------------------------------- //
//                 lib.rs                //
// ------------------------------------- //

// modules
mod gtts;

// use py03
use pyo3::prelude::*;

// define modules
#[pymodule]
#[pyo3(name = "rust")]
fn rust(py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    // add gtts
    let gtts = PyModule::new_bound(py, "gtts")?;
    gtts.add_class::<gtts::TextToSpeech>()?;
    m.add_submodule(&gtts)?;

    Ok(())
}