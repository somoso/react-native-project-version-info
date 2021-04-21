# react-native-project-version-info

Do you need a way to:

* Automate a way of fetching your Android version name or version code?
* Automate a way to get the iOS Version or Build number?
* **Only** need this information **outside** the React Native code? e.g. for automated CI builds?
* Happy to run Python3 code rather than shell scripts?

Then this is the code for you.

## Source code

This project contains two files:

* `parse_android_build.py`
* `parse_ios_build.py`

The minimum requirement for both is Python 3. Other than that, it has no external dependencies (no need to `pip install`
anything). This comes at a cost at the cost being a bit "simple" as it loops over the files line by line trying to get
what it needs. It's simple, but it works.

## Usage instructions

### For parsing the Android build file:

~~~
./parse_android_build.py <version_type> <path>
~~~

where:

* `version_type` is what you are trying to obtain
    * `name` for `versionName` in your build.gradle file
    * `code` for `versionCode` in your build.gradle file
* `path` is the location of the **root** of the react native project directory.

#### Example:

---

~~~
./parse_android_build.py code /tmp/rn_proj
~~~

will return on the terminal:

```
5
```

where `versionCode` was set to `5` in `build.gradle` in the Android project

---

~~~
./parse_android_build.py name /tmp/rn_proj
~~~

will return on the terminal:

```
1.0.1
```

where `versionName` was set to `5` in `build.gradle` in the Android project

---

### For parsing the ios Xcode project file

~~~
./parse_ios_build.py <version_type> <path>
~~~

where:

* `version_type` is what you are trying to obtain
    * `name` for `Version` in your Xcode Project
    * `code` for `Build Number` in your Xcode Project
* `path` is the location of the **root** of the react native project directory.

The syntax for the iOS parsing is similar to Android.

#### Example:

---

~~~
./parse_ios_build.py code /tmp/rn_proj
~~~

will return on the terminal:

```
5
```

where the `Build Number` was set to `5` in the React Native Xcode Project.

---

~~~
./parse_ios_build.py name /tmp/rn_proj
~~~

will return on the terminal:

```
1.0.1
```


where the `Name` was set to `1.0.1` in the React Native Xcode Project.

---

## Caveats

* This hasn't been tested on Expo projects.
* This can break for iOS builds if you haven't modified the `Name` or `Build Number`. 
* It has only been tested on two projects that have been maintained for over a year. This could very well break in the future if React Native change their project structure.
* If you don't have your Android project files in `android` in the root of your RN folder and/or don't have `ios` in the root of your RN folder, then this code will fail.
* The code _can_ be tweaked to get the info from Native iOS and Android projects - I'm just not personally vested in that. 
