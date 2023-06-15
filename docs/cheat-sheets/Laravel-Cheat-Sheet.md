---
title: Laravel Artisan Command Cheat Sheet
description: This cheat sheet provides a list of frequently used Laravel Artisan commands
status: published
tags:
 - laravel
 - cheat sheet
date: 2022-12-09
---
# Laravel Artisan Command Cheat Sheet

This cheat sheet provides a list of frequently used Laravel Artisan commands along with their short descriptions and examples.

| Command | Short Description | Example |
|---------|------------------|---------|
| `php artisan serve` | Starts the Laravel development server. | `php artisan serve` |
| `php artisan migrate` | Runs all pending database migrations. | `php artisan migrate` |
| `php artisan make:model` | Generates a new Eloquent model class. | `php artisan make:model User` |
| `php artisan make:controller` | Generates a new controller class. | `php artisan make:controller UserController` |
| `php artisan make:middleware` | Generates a new middleware class. | `php artisan make:middleware AuthMiddleware` |
| `php artisan make:migration` | Generates a new database migration file. | `php artisan make:migration create_users_table` |
| `php artisan make:seeder` | Generates a new database seeder class. | `php artisan make:seeder UsersTableSeeder` |
| `php artisan tinker` | Opens an interactive shell for Laravel. | `php artisan tinker` |
| `php artisan route:list` | Lists all registered routes. | `php artisan route:list` |
| `php artisan cache:clear` | Clears the application cache. | `php artisan cache:clear` |
| `php artisan config:cache` | Caches the configuration files. | `php artisan config:cache` |
| `php artisan queue:work` | Processes jobs on the queue. | `php artisan queue:work` |
| `php artisan schedule:run` | Runs the scheduled commands. | `php artisan schedule:run` |
| `php artisan optimize` | Optimizes the application for better performance. | `php artisan optimize` |
| `php artisan key:generate` | Generates a new application key. | `php artisan key:generate` |

Note: Make sure to run these commands from the root directory of your Laravel project.