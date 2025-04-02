package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func InitRepo(dir string) error {
	// Check if the directory already exists
	if _, err := os.Stat(filepath.Join(dir, ".git")); err == nil {
		return fmt.Errorf("a Git repository already exists in %s", dir)
	}

	// Create .git directory and subdirectories
	gitDirs := []string{
		".git", ".git/objects", ".git/refs", ".git/hooks", ".git/info",
	}

	for _, d := range gitDirs {
		err := os.MkdirAll(filepath.Join(dir, d), 0755)
		if err != nil {
			return fmt.Errorf("failed to create %s: %v", d, err)
		}
	}

	// Create default files
	files := map[string]string{
		".git/HEAD":        "ref: refs/heads/master\n",
		".git/config":      "[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n",
		".git/description": "Unnamed repository; edit this file to name it.\n",
	}

	for file, content := range files {
		err := os.WriteFile(filepath.Join(dir, file), []byte(content), 0644)
		if err != nil {
			return fmt.Errorf("failed to create %s: %v", file, err)
		}
	}

	fmt.Println("Initialized empty repository in", dir)
	return nil
}
