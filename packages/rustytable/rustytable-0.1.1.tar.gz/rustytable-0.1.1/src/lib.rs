use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[pyclass]
#[derive(Serialize, Deserialize)]
struct Cell {
    value: String,
    color: Option<String>,
    bold: bool,
    align: Option<String>,
    colspan: Option<usize>,
}

#[pymethods]
impl Cell {
    #[new]
    fn new(value: String, color: Option<String>, bold: bool, align: Option<String>, colspan: Option<usize>) -> Self {
        Cell { value, color, bold, align, colspan }
    }
}

#[pyclass]
#[derive(Serialize, Deserialize)]
struct Theme {
    header_color: Option<String>,
    row_colors: Vec<String>,
}

#[pymethods]
impl Theme {
    #[new]
    fn new(header_color: Option<String>, row_colors: Vec<String>) -> Self {
        Theme { header_color, row_colors }
    }
}

#[pyclass]
#[derive(Serialize, Deserialize)]
struct Table {
    headers: Vec<String>,
    rows: Vec<Vec<Cell>>,
    theme: Option<Theme>,
    title: Option<String>,
    subtitle: Option<String>,
    borders: bool,
}

#[pymethods]
impl Table {
    #[new]
    fn new(headers: Vec<String>, theme: Option<Theme>, borders: bool) -> Self {
        Table { headers, rows: Vec::new(), theme, title: None, subtitle: None, borders }
    }

    fn add_row(&mut self, row: Vec<Cell>) {
        self.rows.push(row);
    }

    fn remove_row(&mut self, index: usize) -> PyResult<()> {
        if index < self.rows.len() {
            self.rows.remove(index);
            Ok(())
        } else {
            Err(pyo3::exceptions::PyIndexError::new_err("Row index out of range"))
        }
    }

    fn add_column(&mut self, header: String, default_value: String) {
        self.headers.push(header);
        for row in &mut self.rows {
            row.push(Cell::new(default_value.clone(), None, false, None, None));
        }
    }

    fn remove_column(&mut self, index: usize) -> PyResult<()> {
        if index < self.headers.len() {
            self.headers.remove(index);
            for row in &mut self.rows {
                row.remove(index);
            }
            Ok(())
        } else {
            Err(pyo3::exceptions::PyIndexError::new_err("Column index out of range"))
        }
    }

    fn to_csv(&self) -> String {
        let mut wtr = csv::Writer::from_writer(Vec::new());
        wtr.write_record(&self.headers).unwrap();
        for row in &self.rows {
            let values: Vec<&str> = row.iter().map(|cell| cell.value.as_str()).collect();
            wtr.write_record(values).unwrap();
        }
        let data = String::from_utf8(wtr.into_inner().unwrap()).unwrap();
        data
    }

    fn to_html(&self) -> String {
        let mut html = String::new();
        html.push_str("<table>\n");
        if let Some(title) = &self.title {
            html.push_str(&format!("<caption>{}</caption>\n", title));
        }
        html.push_str("<thead>\n<tr>");
        for header in &self.headers {
            html.push_str(&format!("<th>{}</th>", header));
        }
        html.push_str("</tr>\n</thead>\n<tbody>\n");
        for row in &self.rows {
            html.push_str("<tr>");
            for cell in row {
                html.push_str(&format!("<td>{}</td>", cell.value));
            }
            html.push_str("</tr>\n");
        }
        html.push_str("</tbody>\n</table>");
        html
    }

    fn to_markdown(&self) -> String {
        let mut markdown = String::new();
        markdown.push_str("| ");
        for header in &self.headers {
            markdown.push_str(&format!("{} | ", header));
        }
        markdown.push_str("\n|");
        for _ in &self.headers {
            markdown.push_str(" --- |");
        }
        markdown.push_str("\n");
        for row in &self.rows {
            markdown.push_str("| ");
            for cell in row {
                markdown.push_str(&format!("{} | ", cell.value));
            }
            markdown.push_str("\n");
        }
        markdown
    }

    fn to_string(&self) -> String {
        let mut table = String::new();
        if let Some(title) = &self.title {
            table.push_str(&format!("{}\n", title));
        }
        if let Some(subtitle) = &self.subtitle {
            table.push_str(&format!("{}\n", subtitle));
        }
        table.push_str(&self.format_row(&self.headers, true, None));
        for (i, row) in self.rows.iter().enumerate() {
            table.push_str(&self.format_row(
                &row.iter().map(|cell| self.apply_theme(&cell.value, &cell.color, cell.bold)).collect::<Vec<String>>(),
                false,
                self.theme.as_ref().and_then(|theme| theme.row_colors.get(i % theme.row_colors.len()))
            ));
        }
        table
    }

    fn apply_theme(&self, text: &str, color: &Option<String>, bold: bool) -> String {
        let mut styled_text = String::from(text);
        if let Some(c) = color {
            styled_text = format!("\x1b[38;5;{}m{}\x1b[0m", c, styled_text);
        }
        if bold {
            styled_text = format!("\x1b[1m{}\x1b[0m", styled_text);
        }
        styled_text
    }

    fn format_row(&self, row: &Vec<String>, is_header: bool, row_color: Option<&String>) -> String {
        let mut formatted_row = String::new();
        formatted_row.push_str("+");
        for _ in row {
            formatted_row.push_str(&format!("{:-<15}+", ""));
        }
        formatted_row.push_str("\n|");
        for cell in row {
            let formatted_cell = if is_header {
                self.apply_theme(cell, &self.theme.as_ref().map(|t| t.header_color.clone().unwrap_or_default()), true)
            } else {
                self.apply_theme(cell, &row_color.map(|c| c.clone()), false)
            };
            formatted_row.push_str(&format!("{:<15}|", formatted_cell));
        }
        formatted_row.push_str("\n+");
        for _ in row {
            formatted_row.push_str(&format!("{:-<15}+", ""));
        }
        formatted_row.push_str("\n");
        formatted_row
    }

    fn set_title(&mut self, title: String) {
        self.title = Some(title);
    }

    fn set_subtitle(&mut self, subtitle: String) {
        self.subtitle = Some(subtitle);
    }

    fn sum(&self, column: &str) -> PyResult<f64> {
        let index = self.headers.iter().position(|h| h == column).ok_or_else(|| {
            pyo3::exceptions::PyValueError::new_err("Column not found")
        })?;
        let sum: f64 = self.rows.iter().map(|row| row[index].value.parse::<f64>().unwrap_or(0.0)).sum();
        Ok(sum)
    }

    fn average(&self, column: &str) -> PyResult<f64> {
        let sum = self.sum(column)?;
        let count = self.rows.len();
        if count > 0 {
            Ok(sum / count as f64)
        } else {
            Ok(0.0)
        }
    }

    fn min(&self, column: &str) -> PyResult<f64> {
        let index = self.headers.iter().position(|h| h == column).ok_or_else(|| {
            pyo3::exceptions::PyValueError::new_err("Column not found")
        })?;
        let min = self.rows.iter().map(|row| row[index].value.parse::<f64>().unwrap_or(f64::MAX)).min_by(|a, b| a.partial_cmp(b).unwrap()).unwrap_or(0.0);
        Ok(min)
    }

    fn max(&self, column: &str) -> PyResult<f64> {
        let index = self.headers.iter().position(|h| h == column).ok_or_else(|| {
            pyo3::exceptions::PyValueError::new_err("Column not found")
        })?;
        let max = self.rows.iter().map(|row| row[index].value.parse::<f64>().unwrap_or(f64::MIN)).max_by(|a, b| a.partial_cmp(b).unwrap()).unwrap_or(0.0);
        Ok(max)
    }

    fn conditional_format(&mut self, column: &str, condition: &str, format: &str) -> PyResult<()> {
        let index = self.headers.iter().position(|h| h == column).ok_or_else(|| {
            pyo3::exceptions::PyValueError::new_err("Column not found")
        })?;
        for row in &mut self.rows {
            if row[index].value == condition {
                row[index].value = format.to_string();
            }
        }
        Ok(())
    }

    fn sort_by(&mut self, column: &str, ascending: bool) -> PyResult<()> {
        let index = self.headers.iter().position(|h| h == column).ok_or_else(|| {
            pyo3::exceptions::PyValueError::new_err("Column not found")
        })?;
        if ascending {
            self.rows.sort_by(|a, b| a[index].value.cmp(&b[index].value));
        } else {
            self.rows.sort_by(|a, b| b[index].value.cmp(&a[index].value));
        }
        Ok(())
    }

    fn filter(&self, column: &str, value: &str) -> PyResult<Self> {
        let index = self.headers.iter().position(|h| h == column).ok_or_else(|| {
            pyo3::exceptions::PyValueError::new_err("Column not found")
        })?;
        let filtered_rows = self.rows.iter().filter(|row| row[index].value == value).cloned().collect();
        Ok(Table {
            headers: self.headers.clone(),
            rows: filtered_rows,
            theme: self.theme.clone(),
            title: self.title.clone(),
            subtitle: self.subtitle.clone(),
            borders: self.borders,
        })
    }

    fn paginate(&self, rows_per_page: usize) -> Vec<Self> {
        self.rows.chunks(rows_per_page).map(|chunk| {
            Table {
                headers: self.headers.clone(),
                rows: chunk.to_vec(),
                theme: self.theme.clone(),
                title: self.title.clone(),
                subtitle: self.subtitle.clone(),
                borders: self.borders,
            }
        }).collect()
    }

    fn set_theme(&mut self, theme: Theme) {
        self.theme = Some(theme);
    }

    fn validate(&self) -> PyResult<()> {
        // Example validation: Check if all rows have the same number of cells as headers
        for row in &self.rows {
            if row.len() != self.headers.len() {
                return Err(pyo3::exceptions::PyValueError::new_err("Row length does not match headers length"));
            }
        }
        Ok(())
    }

    fn load_data(&mut self, data: Vec<HashMap<String, String>>) -> PyResult<()> {
        self.headers = data[0].keys().cloned().collect();
        self.rows = data.iter().map(|row| {
            self.headers.iter().map(|header| {
                let value = row.get(header).cloned().unwrap_or_default();
                Cell::new(value, None, false, None, None)
            }).collect()
        }).collect();
        Ok(())
    }
}

#[pyfunction]
fn from_csv(data: &str) -> Table {
    let mut rdr = csv::Reader::from_reader(data.as_bytes());
    let headers = rdr.headers().unwrap().clone();
    let mut table = Table::new(headers.iter().map(|s| s.to_string()).collect(), None, false);
    for result in rdr.records() {
        let record = result.unwrap();
        let row = record.iter().map(|s| Cell::new(s.to_string(), None, false, None, None)).collect();
        table.add_row(row);
    }
    table
}

#[pymodule]
fn rustytable(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Table>()?;
    m.add_class::<Cell>()?;
    m.add_class::<Theme>()?;
    m.add_function(wrap_pyfunction!(from_csv, m)?)?;
    Ok(())
}
