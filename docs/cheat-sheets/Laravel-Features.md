---
title: Laravel features
description: This cheat sheet lists the most used PHP Laravel Framework features.
status: published
tags:
 - sheet
 - laravel
 - php
date: 20230-02-09
---
# Laravel Features
This cheat sheet lists the most used PHP Laravel Framework features.

| Feature Name                            | Short Description                            | Code Example                                                       |
| --------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------ |
| Routing                                 | Define application routes                     | `Route::get('/user/{id}', 'UserController@show');`                 |
| Middleware                              | Handle HTTP requests before reaching routes   | `Route::middleware('auth')->get('/dashboard', 'DashboardController@index');` |
| Controllers                             | Handle user requests and return responses     | `class UserController extends Controller { // Controller logic }`  |
| Views                                   | Display information to the user               | `return view('welcome', ['name' => 'John']);`                      |
| Blade Templates                         | Laravel's template engine                      | `@if(count($records) === 1) { // Show one record } @endif`         |
| Migrations                              | Database schema management                    | `php artisan make:migration create_users_table`                     |
| Eloquent ORM                            | Object-Relational Mapping                     | `User::where('name', 'John')->first();`                            |
| Eloquent Relationships                  | Define relationships between database tables  | `public function posts() { return $this->hasMany('App\Post'); }`    |
| Query Builder                           | Build database queries                        | `DB::table('users')->where('votes', '>', 100)->get();`              |
| Eloquent Query Scopes                   | Reusable query constraints                    | `public function scopePopular($query) { return $query->where('votes', '>', 100); }` |
| Authentication                          | User authentication and authorization         | `Auth::attempt(['email' => $email, 'password' => $password]);`     |
| Authorization                           | Control access to resources                   | `if (Gate::allows('update-post', $post)) { // Update post }`       |
| Validation                              | Validate user input                           | `$validatedData = $request->validate(['name' => 'required|string']);` |
| File Storage                            | Store and retrieve files                      | `$path = $request->file('avatar')->store('avatars');`              |
| Queues                                  | Dispatch jobs for background processing       | `dispatch(new SendEmailJob($user));`                                |
| Events                                  | Trigger and listen for application events     | `event(new UserRegistered($user));`                                 |
| Caching                                 | Store frequently accessed data in cache       | `Cache::put('key', 'value', $seconds);`                            |
| Localization                            | Translate application messages                | `__('messages.welcome');`                                          |
| Error Handling                          | Handle and log application errors             | `try { // Code } catch (Exception $e) { // Handle error }`          |
| Task Scheduling                         | Schedule and run commands periodically        | `schedule(function (ConsoleKernel $kernel) { $kernel->command('foo')->daily(); });` |
| Form Request Validation                 | Validate form data with custom rules          | `public function rules() { return ['email' => 'required|email']; }` |
| Database Seeds                          | Populate database with dummy data             | `php artisan db:seed`                                              |
| API Resources                           | Transform models into API-friendly responses | `return new UserResource(User::find(1));`                           |
| Notifications                           | Send notifications to users                    | `$user->notify(new InvoicePaid($invoice));`                        |
| Testing                                 | Write unit and integration tests              | `public function testLogin() { $response = $this->post('/login', ['email' => 'test@example.com', 'password' => 'password']); $response->assert



