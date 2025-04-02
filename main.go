package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: ccgit <command>")
		return
	}

	switch os.Args[1] {
	case "init":
		if len(os.Args) < 3 {
			fmt.Println("Usage: ccgit init <directory>")
			return
		}
		err := InitRepo(os.Args[2])
		if err != nil {
			fmt.Println("Error:", err)
		}
	default:
		fmt.Println("Unknown command:", os.Args[1])
	}
}
