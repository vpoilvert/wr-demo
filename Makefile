#!make
SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -euc
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.PHONY: sync-raw
sync-raw:
	aws s3 sync --delete raw s3://wescale-pandas-demo/raw

.PHONY: ls-raw
ls-raw:
	aws s3 ls s3://wescale-pandas-demo/raw/ --recursive --human-readable --summarize | grep '.csv.gz$$'

.PHONY: clean
clean:
	rm -rf source/
