use advent::ProblemSolution;

pub fn solve(input: &str) -> ProblemSolution {
    let data = parse(input);
    let p1 = part_one(input);
    let p2 = part_two(input);
    ProblemSolution {
        p1.into(),
        p2.into()
    }
}

pub fn parse(input: &str) -> Vec<i32> {
    input
        .lines()
        .map(|f| f.into())
        .collect()
}

pub fn part_one(input: &[i32]) -> i32 {
    input.iter().map(|x| (x/3)-2).sum()
}

pub fn part_two(input: &[i32]) -> usize {
    let mut floor = 0;
    for (idx, i) in input.iter().enumerate() {
        floor += i;
        if floor == -1 {
            return idx + 1;
        }
    }
    unreachable!();
}