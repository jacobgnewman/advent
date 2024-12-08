use reqwest::blocking::Client;
use reqwest::header::COOKIE;
use reqwest::StatusCode;
use std::{fs, path::PathBuf};

fn get_credentials() -> String {
    let mut path = std::env::current_dir().expect("Can't fetch current dir");
    path.push("input/aoc.session");
    println!("path = {}", path.display());
    fs::read_to_string(path).expect("Failed to read from credential file")
}

fn get_input_path(year: u16, day: u8) -> PathBuf {
    let mut path = std::env::current_dir().expect("Can't fetch current dir");
    path.push(format!("input/{}/day{}.txt", year, day));
    path
}

fn get_input_directory(year: u16, day: u8) -> PathBuf {
    let mut path = std::env::current_dir().expect("Can't fetch current dir");
    path.push(format!("input/{}/{:02}/", year, day));
    path
}

// Fetches the puzzle input for a given day
// Will cache puzzle input once retrieved locally
// NOTE: Relies on a valid sesssion cookie in input/aoc.session
pub fn get_input(year: u16, day: u8) -> String {
    let inp_path = get_input_path(year, day);
    if inp_path.exists() {
        fs::read_to_string(inp_path).expect("Failed to read from input file")
    } else {
        load_input(year, day)
    }
}

fn load_input(year: u16, day: u8) -> String {
    let directories = get_input_directory(year, day);
    fs::create_dir_all(directories).expect("Failed to make directiories");
    let input_url = format!("https://adventofcode.com/{}/day/{}/input", year, day);
    let cookie = format!(
        "session={};User-Agent=github.com/jacobgnewman/advent/ by jacobgnewman001@gmail.com",
        get_credentials()
    );

    let client = Client::new();
    let res = client.get(input_url).header(COOKIE, cookie).send();

    match res {
            Ok(response) => match response.status() {
                StatusCode::OK => {
                    let text = response.text().expect("Failed to get text from respones");
                    let path = get_input_path(year, day);
                    fs::write(path.clone(), text).expect("Failed to write to file");
                    fs::read_to_string(path).expect("Failed to read from file")
                }
                sc => panic!(
                    "Could not find corresponding input. Are the day, year, and token correctly set ? Status: {}", sc
                ),
            },
            Err(e) => panic!("Failed to get a response: {}", e),
        }
}
