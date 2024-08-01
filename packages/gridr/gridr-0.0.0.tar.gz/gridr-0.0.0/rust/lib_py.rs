#![warn(missing_docs)]
//! Crate doc
use pyo3::prelude::*;
use crate::lib_core::mymodule as core_mymodule;
use ndarray;
use numpy::{IntoPyArray, PyArray1, PyArray2, PyArrayDyn, PyReadonlyArrayDyn, PyArrayMethods};

/// We tell here what module/functions we use from the pure rust library (lib.rs)
//use crate::lib_core::*;
 
/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
//#[pymodule]
//mod _mylib {
#[pymodule]
fn _mylib(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(array_func,m)?)?;
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}

/// A numpy imut/mut function
#[pyfunction]
#[allow(clippy::too_many_arguments)]
fn array_func(
    read_arr: &Bound<'_, PyArrayDyn<f64>>,
    write_arr: &Bound<'_, PyArrayDyn<f64>>
) -> Result<(), PyErr> {
    
    // Convert the read only array into ndarray
    let read_arr = read_arr.readonly();
    let read_arr = read_arr.as_array(); //.expect("read_arr is not contiguous");
    
    // Make the write_arr mutable
    let mut write_arr = write_arr.readwrite();
    let mut write_arr = write_arr.as_array_mut();
    
    //println!("Before function call...");
    //println!("{}", read_arr[0].to_string());
    //println!("{}", read_arr.len().to_string());
    //println!("{}", write_arr.len().to_string());
    core_mymodule::an_array_func(&read_arr.view(), &mut write_arr.view_mut());
    Ok(())
    /* match core_mymodule::an_array_func(&read_arr, &write_arr) {
      Ok(()) => {
          println!("Computation ok");
          Ok(())
          },
      _ => {
          println!("Computation not ok");
          Ok(())
          }
    } */
}

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    core_mymodule::sum_a_b_str(a as f64,b as f64)
    //Ok((a + b).to_string()
}

