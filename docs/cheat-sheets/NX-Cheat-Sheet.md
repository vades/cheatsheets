---
title: NX Commands Cheat Sheet
description: This cheat sheet covers a range of common NX commands used in an Angular workspace
status: published
tags:
 - angular
 - nx
 - cheat sheet
date: 2022-09-22
---
# NX Commands Cheat Sheet

This cheat sheet covers a range of common NX commands used in an Angular workspace, allowing you to efficiently perform various tasks such as building, serving, testing, generating code, linting, and managing the workspace.

| Command         | Short Description                  | Example                                       |
| --------------- | --------------------------------- | --------------------------------------------- |
| `nx build`      | Build an Angular workspace        | `nx build my-app`                             |
| `nx serve`      | Serve an Angular application       | `nx serve my-app`                             |
| `nx test`       | Run tests for an Angular project   | `nx test my-app`                              |
| `nx generate`   | Generate code using schematics     | `nx generate component my-component`          |
| `nx lint`       | Lint the codebase                  | `nx lint my-app`                              |
| `nx run`        | Execute a project task             | `nx run my-app:task`                          |
| `nx dep-graph`  | Generate a dependency graph        | `nx dep-graph`                                |
| `nx list`       | List available projects or tasks    | `nx list`                                     |
| `nx affected`   | Run tasks for affected projects    | `nx affected:build`                           |
| `nx workspace`  | Manage the Angular workspace       | `nx workspace schematic my-schematic`         |

Note: Replace `my-app`, `my-component`, `task`, `my-schematic`, etc. with your project-specific names.