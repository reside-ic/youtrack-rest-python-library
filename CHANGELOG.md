# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2019-22-4
### Added
- Named tuples for
   - Issues
   - Projects
   - Commands
- Create issue functionality
- Run YouTrack command functionality
- Get issues functionality
- Get projects functionality

### Changed
- Changed the original [License](https://github.com/JetBrains/youtrack-rest-python-library/blob/master/LICENSE) to a MIT [License](https://github.com/JoshLee0915/youtrack-rest-python-library/blob/master/LICENSE)
- Updated the original setup.py to install YTClient from youtrack & youtrack.sync 
- Setup.py now requires python 3.6+
- Updated readme to provide information on YTClient instead of [youtrack-rest-python-library](https://github.com/JetBrains/youtrack-rest-python-library)

### Removed
- youtrack & youtrack.sync
- JBOfficial tag from README
- MANIFEST.in