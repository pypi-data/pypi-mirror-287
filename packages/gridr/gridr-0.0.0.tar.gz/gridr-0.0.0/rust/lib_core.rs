#![warn(missing_docs)]
//! Crate doc
//use ndarray as nd;
/// Add python binding in the scope

/// Current module
pub mod mymodule {
    use ndarray::prelude::*;
    use ndarray::{ArrayViewD, ArrayViewMutD};
    //use numpy::ndarray::{ArrayViewD, ArrayViewMutD};
    
    /// Function sum_a_b_str
    pub fn sum_a_b_str<E>(a: f64, b: f64) -> Result<String, E> {
        let s = a + b;
        //s.to_string()?
        Ok(s.to_string())
    }
    
    pub fn an_array_func(
            an_imut_array: &ArrayViewD<'_, f64>,
            a_mut_array: &mut ArrayViewMutD<'_, f64>) -> i32 {
        
        if a_mut_array.len() != an_imut_array.len() {
            panic!("both arrays must share same length")
        }
        a_mut_array.slice_mut(s![..]).assign(&(&an_imut_array.slice(s![..]) * 2.0));
        //a_mut_array[0] = an_imut_array[0] * 2.0;
        //a_mut_array[1] = an_imut_array[1] * 2.0;
        let ret = 1;
        ret
    }
}

