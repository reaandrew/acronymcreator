## [1.5.4](https://github.com/reaandrew/acronymcreator/compare/v1.5.3...v1.5.4) (2025-06-15)

### Bug Fixes

* exclude docs/scripts from SonarCloud coverage analysis ([2574c58](https://github.com/reaandrew/acronymcreator/commit/2574c58df0838b74abbb977fcfc08d34f2f5bb7c))
* standardize GitGuardian API key environment variable name ([37458ec](https://github.com/reaandrew/acronymcreator/commit/37458ec007751287383ec21279319d3cc6c53653))
* use non-interactive matplotlib backend in graph script ([6d071b4](https://github.com/reaandrew/acronymcreator/commit/6d071b40940068225da2ef96ea5275bb2fdd1035))

## [1.5.3](https://github.com/reaandrew/acronymcreator/compare/v1.5.2...v1.5.3) (2025-06-13)

### Bug Fixes

* explicitly exclude tests and setup.py from SonarCloud source analysis ([5d9d9b2](https://github.com/reaandrew/acronymcreator/commit/5d9d9b2d16478479e8ee3a6d20116c4e4f9340df))

## [1.5.2](https://github.com/reaandrew/acronymcreator/compare/v1.5.1...v1.5.2) (2025-06-13)

### Bug Fixes

* align SonarCloud source analysis with local coverage scope ([46bfe88](https://github.com/reaandrew/acronymcreator/commit/46bfe8891d52bef7253238497698feeb16b391d3))

## [1.5.1](https://github.com/reaandrew/acronymcreator/compare/v1.5.0...v1.5.1) (2025-06-13)

### Bug Fixes

* improve SonarCloud quality gate handling and debugging ([4d2f8ab](https://github.com/reaandrew/acronymcreator/commit/4d2f8ab2f4c0400ab9787a6f878bb93e8ea0decf))

## [1.5.0](https://github.com/reaandrew/acronymcreator/compare/v1.4.0...v1.5.0) (2025-06-13)

### Features

* implement multiple acronym options generation ([b68301b](https://github.com/reaandrew/acronymcreator/commit/b68301b4e4464d7d82281cf4c1a7004915a92e40))
* implement syllable-based acronym generation ([7f11c2f](https://github.com/reaandrew/acronymcreator/commit/7f11c2f93cb160b5c029a44aa842aacff14db968))

## [1.4.0](https://github.com/reaandrew/acronymcreator/compare/v1.3.0...v1.4.0) (2025-06-13)

### Features

* implement word extraction and filtering functionality ([1794e8a](https://github.com/reaandrew/acronymcreator/commit/1794e8afe1a722b44c8005a3b31680195a828a9b))

## [1.3.0](https://github.com/reaandrew/acronymcreator/compare/v1.2.2...v1.3.0) (2025-06-13)

### Features

* integrate Semgrep security analysis into CI pipeline ([8cfb990](https://github.com/reaandrew/acronymcreator/commit/8cfb990d3ef0e8c21bbf2bd8f215d57f62f1cf5d))

## [1.2.2](https://github.com/reaandrew/acronymcreator/compare/v1.2.1...v1.2.2) (2025-06-12)

### Bug Fixes

* configure Flake8 line length to match Black (88 chars) ([3d07c41](https://github.com/reaandrew/acronymcreator/commit/3d07c41234b2ceb00fca86c063e978547a770f6d))

## [1.2.1](https://github.com/reaandrew/acronymcreator/compare/v1.2.0...v1.2.1) (2025-06-12)

### Bug Fixes

* correct pytest config section header and remove test code ([85c0a2c](https://github.com/reaandrew/acronymcreator/commit/85c0a2c1c9df3f265e5a462838753cc7b8eb940d))
* prevent pytest coverage from creating files in pre-commit ([ac033cc](https://github.com/reaandrew/acronymcreator/commit/ac033cc555529c3f2a03fd8a1f263ee40d73351f))
* prevent pytest from creating cache files during pre-commit ([40f148d](https://github.com/reaandrew/acronymcreator/commit/40f148d651d8960094236e6a51c5309914f54965))
* use .coveragerc to properly redirect coverage data file ([e0bbfbc](https://github.com/reaandrew/acronymcreator/commit/e0bbfbc08b373b3bbae22efb642e2dfd6a814ad4))

## [1.2.0](https://github.com/reaandrew/acronymcreator/compare/v1.1.0...v1.2.0) (2025-06-12)

### Features

* add complete Python package structure and CLI ([d7c4cd4](https://github.com/reaandrew/acronymcreator/commit/d7c4cd4e888c1466c09c1c377c9fc90801d04386))
* add detailed SonarCloud quality gate status reporting ([add571c](https://github.com/reaandrew/acronymcreator/commit/add571c920b28ba3a72fe943a79c8872582a7cf5))
* implement article filtering for acronym generation ([2f96c4f](https://github.com/reaandrew/acronymcreator/commit/2f96c4fd5de000148e14e4252812896ee734e490))

### Bug Fixes

* configure pytest pre-commit hook for CI compatibility ([58f9331](https://github.com/reaandrew/acronymcreator/commit/58f9331d5095a3e3cc932217b08b38ce4ab48d55))
* configure pytest pre-commit hook to show Passed when coverage is good ([d8e33d3](https://github.com/reaandrew/acronymcreator/commit/d8e33d345aece8962c291567a5ddc49a83ca10b5))
* install project dependencies including click in CI ([ba87333](https://github.com/reaandrew/acronymcreator/commit/ba873333da38f8d08652c993f75dd1a366e7f7e6))
* update repository URL in semantic-release config ([6ea0983](https://github.com/reaandrew/acronymcreator/commit/6ea0983e33462a10ed3ca0c1c139040062d3301b))

## [1.1.0](https://github.com/reaandrew/git-guardian-ci-examples/compare/v1.0.1...v1.1.0) (2025-06-12)

### Features

* add initial acronym creator with basic functionality ([c68b2e0](https://github.com/reaandrew/git-guardian-ci-examples/commit/c68b2e08a675e563dcdc89394f2b177ee4ccad37))
* add SonarCloud analysis with improved CI stage naming ([b0fbb39](https://github.com/reaandrew/git-guardian-ci-examples/commit/b0fbb397d1aa46422981d4fadedc209dacffb986))

### Bug Fixes

* remove trailing whitespace from README ([9e49825](https://github.com/reaandrew/git-guardian-ci-examples/commit/9e49825a0043412bbede68a13a2080c55640597c))

## [1.0.1](https://github.com/reaandrew/git-guardian-ci-examples/compare/v1.0.0...v1.0.1) (2025-06-12)

### Bug Fixes

* update pre-commit hooks to resolve deprecation warnings ([a5c9773](https://github.com/reaandrew/git-guardian-ci-examples/commit/a5c9773daddcbfa6108d2f9a09fc8accca70ec9a))

## 1.0.0 (2025-06-12)

### Features

* add basic GitHub Actions CI workflow ([5db32ca](https://github.com/reaandrew/git-guardian-ci-examples/commit/5db32ca5217326700d043c9c943dc991aab930fe))
* add conventional commit enforcement with pre-commit ([a1cbbf1](https://github.com/reaandrew/git-guardian-ci-examples/commit/a1cbbf1270981369f3b3659f0baaa79c3c91a5fc))
* add semantic-release for automated versioning and tagging ([828c9b9](https://github.com/reaandrew/git-guardian-ci-examples/commit/828c9b994c10e55e7462e1aee402abd6b8d54602))
* add test file for demonstrating pre-commit validation ([ab30896](https://github.com/reaandrew/git-guardian-ci-examples/commit/ab308966ec3a45b63e28c604624d2b3bb0775709))

### Bug Fixes

* add missing conventional-changelog dependency and fix semantic-release config ([de1c5c7](https://github.com/reaandrew/git-guardian-ci-examples/commit/de1c5c7dc79871f5443fedcdb2aaa22f542e20d4))
