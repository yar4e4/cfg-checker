package main

import (
	"fmt"
	"os"

	"gopkg.in/yaml.v3"
)

type Config struct {
	Version string `yaml:"version"`
	Host    string `yaml:"host"`
	Port    int    `yaml:"port"`
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: config-validator <config.yaml>")
		os.Exit(1)
	}

	configPath := os.Args[1]

	data, err := os.ReadFile(configPath)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to read file %s: %v\n", configPath, err)
		os.Exit(1)
	}

	var cfg Config
	if err := yaml.Unmarshal(data, &cfg); err != nil {
		fmt.Fprintf(os.Stderr, "Failed to parse YAML: %v\n", err)
		os.Exit(1)
	}

	var validationErrors []string

	if cfg.Version == "" {
		validationErrors = append(validationErrors, "field 'version' is required")
	}

	if cfg.Host == "" {
		validationErrors = append(validationErrors, "field 'host' is required")
	}

	if cfg.Port < 1 || cfg.Port > 65535 {
		validationErrors = append(validationErrors, fmt.Sprintf("port must be between 1 and 65535, got %d", cfg.Port))
	}

	if len(validationErrors) > 0 {
		fmt.Fprintln(os.Stderr, "Validation failed:")
		for _, errMsg := range validationErrors {
			fmt.Fprintf(os.Stderr, "  - %s\n", errMsg)
		}
		os.Exit(1)
	}

	fmt.Println("Configuration is valid")
}