#![allow(clippy::unused_unit)]

use polars::prelude::*;
use pyo3::prelude::*;
use pyo3_polars::PolarsAllocator;
use pyo3_polars::derive::polars_expr;
use whichlang::detect_language;

#[global_allocator]
static ALLOC: PolarsAllocator = PolarsAllocator::new();

// #[pymodule]
// fn _internal(_py: Python, _m: &Bound<PyModule>) -> PyResult<()> {
//     Ok(())
// }

#[polars_expr(output_type=String)]
fn detect_lang(inputs: &[Series]) -> PolarsResult<Series> {
    let ca: &StringChunked = inputs[0].str()?;
    let out: StringChunked = ca.apply_into_string_amortized(|value: &str, output: &mut String| {
        let lang = detect_language(value);
        let code = lang.three_letter_code();
        output.push_str(code);
    });
    Ok(out.into_series())
}
