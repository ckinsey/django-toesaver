django-toesaver
===============

Keep users from stepping on each other's toes!

django-toesaver provides an API and tools for rendering a moderately responsive list of users who are browsing the same
page of an application.  Useful for letting users know when "somebody else is editing this content" a la Google Docs or Atlassian Confluence.


Requirements
------------

**jQuery**

Should work with pretty old versions because the usage is basic, but it's only tested against jQuery 1.10. YMMV

**Cache Backend**

Per-page user lists are stored in your cache backend.  This is really only intended to be used for small projects
with a limited audience size (admin users, etc).  I advise using an in-memory cache like memcached because it could
get a bit database intensive at scale.

Quick Start
-----------
*   Add `'toesaver'` to `INSTALLED_APPS`
*   Set up the relevant settings, defined in seconds:

    ```python
    # How often do we check the backend for new viewers
    TOESAVER_POLL_FREQUENCY = 5

    # How long after a user stops checking in do we consider them dead?
    TOESAVER_VIEW_TIMEOUT = 30
    ```
*   Add the toesaver urls to your URL conf:

    `url(r'^toesaver/', include('toesaver.urls')),`

*   Set up a callback JS method to do something with the user list
    This method must be called `toesaver_poll_callback` and accepts one argument, an array of usernames:
    ```javascript
    function toesaver_poll_callback(users) {
        console.log(users);
        $("#userHolder").html(users);
        // or whatever
    }
    ```
*   Call the `save_those_toes` template tag somewhere AFTER your callback method is defined on the template:
    ```html
    <script type="text/javascript">
    function toesaver_poll_callback(u){ /*...*/ }
    </script>

    {% load toesaver_tags %}
    {% save_those_toes %}
    ```
*   Eat a donut.  You're done!
