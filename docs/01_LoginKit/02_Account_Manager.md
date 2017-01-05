
## Overview

{% method %}

Access `AccountManager` instance:

{% sample lang="Android" %}

```java
AccountManager accountManager = LoginKit.getAccountManager();
```
> **Notice that** to use apis under `AccountManager`, you must ensure that
user already logged in, to check if user logged in or not, use `AccountManager.isLoggedIn()`
method.

{% sample lang="IOS" %}

Updating...

{% endmethod %}

## Managing account profiles
With `LoginKit`, every account can have multiple profiles. After `user` logged in,
you can access all profile of their account by using `ProfileManager.getAccountProfiles()`:

{% method %}

### Get all profiles

{% sample lang="Android" %}

```java
LoginKit.getAccountManager().getAccountProfiles()
    .flatMap(listProfile -> Observable.from(listProfile))
    .subscribeOn(Schedulers.io())
    .subscribe(profile -> {
        // do on each profile
        Log.d("AccountProfile", profile.toString());
    }, Throwable::printStackTrace);
```

{% sample lang="IOS" %}

Updating...

{% endmethod %}

{% method %}

### Create new profile
To create new profile for current account, use `AccountManager.createNewProfile()`.

{% sample lang="Android" %}

```java
// create vip profile for current account.
ProfileProperties profileProps = ImmutableProfileProperties.builder()
        .name("John")  
        .putProperties("account_type", "vip_account")
        .build();
LoginKit.getAccountManager().createNewProfile(profileProps,
        newProfile -> Log.d("CreateProfile", "Success: " + newProfile));
```
After profile is created, `LoginKit` uses it as activating profile by default, you
can check the current active profile via `AccountManager.getCurrentActiveProfileId()`.
{% sample lang="IOS" %}

Updating...

{% endmethod %}

{% method %}

### Switch to another profile

Then in case you want to switch to another available profile, `LoginKit` has method
to switch to any profile with specific `id`.

{% sample lang="Android" %}
```java
LoginKit.getAccountManager().switchToProfile("another_profile_id",
        newAuthToken -> System.out.println(newAuthToken),
        Throwable::printStackTrace);
```
After switching profile succeed, `AccountManager.getCurrentActiveProfileId()` should
return the value `"another_profile_id"`.

{% sample lang="IOS" %}

Updating...

{% endmethod %}
