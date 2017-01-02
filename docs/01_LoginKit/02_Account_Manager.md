[TOC]

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

## Account profiles
With `LoginKit`, every account can has multiple profiles. After `user` already logged in,
you can access all profile of their account.

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

### Create new one
To create new profile for current account, use `AccountManager.createNewProfile()`.
After profile is created, `LoginKit` uses it as activating profile by default.

{% sample lang="Android" %}

```java
// create vip profile for current account.
ProfileProperties profileProps = ImmutableProfileProperties.builder()
        .name("John")  
        .avatar(avatarFile)
        .putProperties("account_type", "vip_account")
        .build();
LoginKit.getAccountManager().createNewProfile(profileProps,
        newProfile -> Log.d("CreateProfile", "Success: " + newProfile));
```

{% sample lang="IOS" %}

Updating...

{% endmethod %}
