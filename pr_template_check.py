#!/usr/bin/env python3
"""Verify PR description follows template"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Verify PR description follows template")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("pr-template-check v0.1.0");return
 print(f"[12:00] pr-template-check ready")
if __name__=="__main__":main()
