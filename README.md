# grepPy

Search for a certain string (substring) in a set of files.

### Usecase

Let's say that you have to find your password in a github repository before pushing it. Start greppy, type in the absolute path of the entire directory, and then type in the string that you are looking for. The application then searches through each file and ignores binary/unsupported types to find what you are looking for. The output is **the files that contain the searched string** and the **index/occurrence count.**

## Getting Started

To set up and run, copy and paste in a new Terminal window:

```bash
git clone https://www.github.com/VladUsatii/greppy.git
cd greppy
chmod +x search.py
./search.py
```

**Output:**

```bash
Enter the directory to search for a string:
[ Directory found ]
Enter the string to search for in the files:
[ String added ]
[ Searching files ... ]

# example find scenario
[ file type '*.txt' • file '<_io.TextIOWrapper name...' • line 0 ]
...

100 occurrences of the string 'apple'
[ All done! ]

[ If command is redone with --remove-all, greppy will remove all occurrences in all files in subdirectories of searched parent directory ]
```

## Unit Tests

Currently setting up a testing environment. Trying to figure out best way to minimize throughput through tree layout.

## Contributions

To contribute, please submit a pull request. All ideas considered.

---
Created by Vlad Usatii @ youshould.readproduct.com
