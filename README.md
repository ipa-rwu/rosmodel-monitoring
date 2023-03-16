# Rosmodel-monitoring

## Setup
```
# install venv
python3 -m venv venv
```
```
# import git submodule
git submodule update
```
```
# install packages
./install.sh
```
```
# regenerate rosmodel from ecore:
# ./gen_metamodel_pyecore.sh "repo name" "branch name of https://github.com/ipa-nhg/ros-model" "folder"
./gen_metamodel_pyecore.sh ipa-rwu/ros-model rwu/fix/YamlMigrationSystem pythonic-rosmodel/pythonic_rosmodel/metamodel_gen
```
