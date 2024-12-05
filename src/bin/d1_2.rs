// historian hysteria (part 2)
use std::{collections::HashMap, fs};

use itertools::Itertools;

fn parse_line(line: &str) -> (i32, i32) {
    let vec = line
        .split_whitespace()
        .map(|num| num.parse::<i32>().expect("Please enter valid numbers"))
        .collect::<Vec<i32>>();
    (vec[0], vec[1])
}

fn main() {
    let contents = fs::read_to_string("inputs/d1").expect("Failed to read file");
    let pairs: Vec<(i32, i32)> = contents.lines().map(parse_line).collect();
    let (left, right): (Vec<i32>, Vec<i32>) = pairs.into_iter().unzip();
    let right: HashMap<i32, usize> = right.into_iter().counts_by(|loc_id| loc_id);
    let total: i32 = left
        .into_iter()
        .map(|loc_id| {
            loc_id * right.get(&loc_id).map_or(0, |&count| i32::try_from(count).unwrap_or(0))
        })
        .sum();

    println!("{}", total);
}
