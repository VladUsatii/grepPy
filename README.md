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
Enter absolute path of parent directory: __ Enter here __
Found __abspath__
What pattern are you looking for?: __ Enter here __

Searching. . .

Found __numofoccurrences__ occurrences in __file1found__
  * Line __linenum__ at index __indexnum__
	..

Found __numofoccurrences__ occurrences in __file2found__
..

All done!

[ If command is redone with --remove-all, greppy will remove all occurrences in all files in subdirectories of searched parent directory ]
```

## Unit Tests

Currently setting up a testing environment.

## Contributions

To contribute, please submit a pull request. All ideas considered.

---
Created by Vlad Usatii @ youshould.readproduct.com
