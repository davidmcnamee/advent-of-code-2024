// red-nosed reports (part 1)
use std::fs;

use itertools::{EitherOrBoth, Itertools};

fn is_safe(raw_report: &str) -> bool {
    let report: Vec<i32> =
        raw_report.split_whitespace().map(|num| num.parse::<i32>().unwrap()).collect();
    if report.is_empty() {
        return true;
    }
    let (is_asc, is_bounded): (Vec<Option<bool>>, Vec<bool>) = report
        .iter()
        .zip_longest(&report[1..])
        .map(|pair| match pair {
            EitherOrBoth::Right(_) => (None, true),
            EitherOrBoth::Left(_) => (None, true),
            EitherOrBoth::Both(a, b) => (Some(a < b), 1 <= (a - b).abs() && (a - b).abs() <= 3),
        })
        .unzip();
    is_asc.iter().filter_map(|&a| a).all_equal() && is_bounded.iter().all(|&b| b)
}

fn main() {
    let contents = fs::read_to_string("inputs/d2_1").expect("Failed to read file");
    let raw_reports: Vec<&str> = contents.trim().split("\n").collect();

    let total_safe = raw_reports.into_iter().filter(|raw_report| is_safe(raw_report)).count();
    println!("{}", total_safe);
}
