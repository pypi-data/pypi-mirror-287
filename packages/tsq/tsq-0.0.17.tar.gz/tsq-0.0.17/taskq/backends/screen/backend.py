import os
import argparse

import flask


class ScreenBackendServer:
    def __init__(self, screen_dir):
        super().__init__()
        self.screen_dir = screen_dir

    def poll(self):
        ...


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['serve', ''])


if __name__ == '__main__':
