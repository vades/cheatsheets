---
title: Angular CLI Cheat Sheet
description: This cheat sheet provides a list of frequently used Angular CLI commands
status: published
tags:
 - angular
 - cheat sheet
date: 2023-02-15
---
# Angular CLI Cheat Sheet

This cheat sheet provides a list of frequently used Angular CLI commands along with a short description and an example for each command.

| Command                             | Description                                       | Example                                                                |
| ----------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------- |
| `ng new <project-name>`             | Creates a new Angular project                           | `ng new my-app`                                                        |
| `ng generate component <name>`       | Generates a new component                                | `ng generate component my-component`                                   |
| `ng serve`                          | Starts the development server                           | `ng serve`                                                             |
| `ng build`                          | Builds the Angular application for production           | `ng build --prod`                                                      |
| `ng test`                           | Runs unit tests                                          | `ng test`                                                              |
| `ng lint`                           | Lints the project's code                                 | `ng lint`                                                              |
| `ng add <package>`                  | Adds a package to the project                            | `ng add @angular/material`                                             |
| `ng update`                         | Updates the dependencies of the project                  | `ng update @angular/cli`                                               |
| `ng generate module <name>`          | Generates a new module                                   | `ng generate module my-module`                                         |
| `ng generate service <name>`         | Generates a new service                                  | `ng generate service my-service`                                       |
| `ng generate directive <name>`       | Generates a new directive                                | `ng generate directive my-directive`                                   |
| `ng generate pipe <name>`            | Generates a new pipe                                     | `ng generate pipe my-pipe`                                             |
| `ng generate class <name>`           | Generates a new class                                    | `ng generate class my-class`                                           |
| `ng generate interface <name>`       | Generates a new interface                                | `ng generate interface my-interface`                                   |
| `ng generate enum <name>`            | Generates a new enum                                     | `ng generate enum my-enum`                                             |
| `ng generate guard <name>`           | Generates a new route guard                              | `ng generate guard my-guard`                                           |
| `ng generate resolver <name>`        | Generates a new route resolver                           | `ng generate resolver my-resolver`                                     |
| `ng generate interceptor <name>`     | Generates a new HTTP interceptor                         | `ng generate interceptor my-interceptor`                               |
| `ng generate component <name> --route` | Generates a new component and creates a routing configuration | `ng generate component my-component --route`                        |
| `ng generate module <name> --routing` | Generates a new module with a routing configuration      | `ng generate module my-module --routing`                              |
| `ng build --watch`                  | Builds and watches for changes in files                  | `ng build --watch`                                                     |
| `ng serve --open`                   | Starts the development server and opens the browser      | `ng serve --open`                                                      |

Remember to run these commands from the command line in the root directory of your Angular project.