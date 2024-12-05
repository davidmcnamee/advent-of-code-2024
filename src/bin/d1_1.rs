// historian hysteria (part 1)
use std::fs;

fn parse_line(line: &str) -> (i32, i32) {
    let vec = line
        .split_whitespace()
        .map(|num| num.parse::<i32>().expect("Please enter valid numbers"))
        .collect::<Vec<i32>>();
    (vec[0], vec[1])
}

fn main() {
    let contents = fs::read_to_string("inputs/d1_1").expect("Failed to read file");
    let pairs: Vec<(i32, i32)> = contents.lines().map(parse_line).collect();
    let (mut left, mut right): (Vec<i32>, Vec<i32>) = pairs.into_iter().unzip();
    left.sort();
    right.sort();
    let pairs = left.into_iter().zip(right);
    let total: i32 = pairs.map(|(a, b)| (a - b).abs()).sum();

    println!("{}", total);
}
