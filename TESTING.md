# Testing strategy for Aquascape Haven

+ Full disclosure - I have not used TDD for all of my apps as I'm sure you can see I have created numerous and wanted to ensure all the TDD I did was processed properly meaning i ran out of time to do all of them.

## Community App

### Post Creation:

+ Authenticated user can create posts
+ Posts require a content field filled in
+ Anonymous user are redirected to log in

### How to run tests:

+ run `python manage.py test community.tests.test_view` in the terminal.

### What happened when i ran tests:

(venv) C:\Users\14sam\.vscode\aquascape-haven>python manage.py test community.tests.test_view
Found 3 test(s).
Creating test database for alias 'default'...
System check identified some issues:

WARNINGS:
?: (account.W001) ACCOUNT_LOGIN_METHODS conflicts with ACCOUNT_SIGNUP_FIELDS

System check identified 1 issue (0 silenced).
EEE
======================================================================
ERROR: test_anonymous_user_cannot_post (community.tests.test_view.TestCommunityViews.test_anonymous_user_cannot_post)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\14sam\.vscode\aquascape-haven\community\tests\test_view.py", line 29, in test_anonymous_user_cannot_post
    response = self.client.post(reverse('community:create_post'), {
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 1153, in post
    response = super().post(
               ^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 499, in post
    return self.generic(
           ^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 671, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 1087, in request
    self.check_exception(response)
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 802, in check_exception
    raise exc_value
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\community\views.py", line 15, in create_post      
    post.user = request.user
    ^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 291, in __set__
    raise ValueError(
ValueError: Cannot assign "<SimpleLazyObject: <django.contrib.auth.models.AnonymousUser object at 0x0000016D463515E0>>": "Community.user" must be a "User" instance.

======================================================================
ERROR: test_logged_in_user_can_post (community.tests.test_view.TestCommunityViews.test_logged_in_user_can_post)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.UndefinedColumn: column "title" of relation "community_community" does not exist 
LINE 1: INSERT INTO "community_community" ("user_id", "title", "cont...
                                                      ^


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\14sam\.vscode\aquascape-haven\community\tests\test_view.py", line 12, in test_logged_in_user_can_post
    response = self.client.post(reverse('community:create_post'), {
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 1153, in post
    response = super().post(
               ^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 499, in post
    return self.generic(
           ^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 671, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 1087, in request
    self.check_exception(response)
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 802, in check_exception
    raise exc_value
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\community\views.py", line 16, in create_post      
    post.save()
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\models\base.py", line 902, in save
    self.save_base(
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\models\base.py", line 1008, in save_base
    updated = self._save_table(
              ^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\models\base.py", line 1169, in _save_table
    results = self._do_insert(
              ^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\models\base.py", line 1210, in _do_insert
    return manager._insert(
           ^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\models\query.py", line 1868, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\models\sql\compiler.py", line 1882, in execute_sql
    cursor.execute(sql, params)
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\backends\utils.py", line 79, in execute
    return self._execute_with_wrappers(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\backends\utils.py", line 92, in _execute_with_wrappers
    return executor(sql, params, many, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\backends\utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django.db.utils.ProgrammingError: column "title" of relation "community_community" does not exist
LINE 1: INSERT INTO "community_community" ("user_id", "title", "cont...
                                                      ^


======================================================================
ERROR: test_post_requires_content (community.tests.test_view.TestCommunityViews.test_post_requires_content)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\14sam\.vscode\aquascape-haven\community\tests\test_view.py", line 21, in test_post_requires_content
    response = self.client.post(reverse('community:create_post'), {
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 1153, in post
    response = super().post(
               ^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 499, in post
    return self.generic(
           ^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 671, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 1087, in request
    self.check_exception(response)
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\test\client.py", line 802, in check_exception
    raise exc_value
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\base.py", line 204, in _get_response
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\base.py", line 204, in _get_response
    self.check_response(response, callback)
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\base.py", line 332, in check_response
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\base.py", line 204, in _get_response
    self.check_response(response, callback)
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\base.py", line 332, in check_response
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\base.py", line 204, in _get_response
    self.check_response(response, callback)
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\base.py", line 332, in check_response
    self.check_response(response, callback)
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\base.py", line 332, in check_response
  File "C:\Users\14sam\.vscode\aquascape-haven\venv\Lib\site-packages\django\core\handlers\base.py", line 332, in check_response
    raise ValueError(
ValueError: The view community.views.create_post didn't return an HttpResponse object. It returned None instead.


----------------------------------------------------------------------
Ran 3 tests in 6.355s

FAILED (errors=3)
Destroying test database for alias 'default'...

### Fixing issues with tests:

+ First issue found in first test was that i was using a test log in but i had not verified it as a logged in user so it was throwing an error stating it was an unauthorised user therefore failing. Fixed issue by adding the line `self.assertTrue(logged_in)`.
+ This was still causing an issues so after reading some documentation on GitHub I found I could use a `self.client.force_login(self.user)` to bypass this issue and allow my tests to run.
+ The next error was because I had not run `python manage.py makemigrations community` and `python manage.py migrate` meaning the DB could not be found.
+ There was also an error regarding the anonymous user posting test failed as I had not added the `@login_required` attribute to the view.
+ Then I found an error for a lack of a `HttpResponse` for `create_post` meaning there was no return after the first section of the view. Once I added an else statement to return to the create post page when when it fails. This then worked.
+ This showed me a reverse not found error. Meaning I had set the view function with an incorrect pattern name or not put the correct include in my project root urls.py file. Once I had set the correct urls.py line and set the `base.html` url to 'Community' up with the correct namespaced url it fixed that error.
+ Then I found an AttributeError for no 'is_bound' attribute. This truns out not to be an issue with my view but actually an issue with my test inteslf as it needed to include the 'form' in the test otherwise it is not grabbing the context as required.
+ Finally 3 tests ran in 6.418ms with no issues.
