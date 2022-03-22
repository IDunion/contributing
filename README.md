# Contributing
The purpouse of this repository is to document what is needed for a (Hyper Ledger) open source contribution.

## License

The most important part is to clearly state

- That the work is copy righted
- Creation Date of the work (maybe a time period)
- Who is the copy right holder

This is done by Adding a line like `Copyright [year(s)] by [author(s)/company(s)]` to at least the Readme of the project. It is usually recommended to even add this to every source file. It should also be visible in the artifacts.

Next to this copy right there should be a statement of the license under which others can use this work. This is typically some minimal description and a link to the full license text, typically shipped in the [LICENSE](./LICENSE) file. Here we use the Apache 2 License, which has an example of what to include in the README/every file at the bottom (slightly adapted):

    Copyright 2020-2022 by all parties listed in the NOTICE file
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this work except in compliance with the License.
    You may obtain a copy of the License at
    
       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

## Notice

Instead of updating all copyright holders everywhere, it is useful to refer to a list of contributors. Typically provided in the [NOTICE](./NOTICE) file. See there for more information about the format.

## Contributors Consent

It is important that all contributors consent to opensourcing the work. To ensure this, you need to explain what contributors agree to. Typically in a [CONTRIBUTING](./CONTRIBUTING.md) file. If you want the Developer Certificate of Origin (DCO) mechanism (see below) this is a good place to explain it. See the attached one for details.

## DCO

This is explained in [CONTRIBUTING](./CONTRIBUTING.md). Most importantly: Make your contributors state that every (original) commit includes in its commit message a statement which expresses the authors consent to the rules layed out in the [CONTRIBUTING](./CONTRIBUTING.md) file. Typically this is done by adding a line like
```
Signed-off-by: Random J Developer <random@developer.example.org>
```
which is automatically added by git if you commit with the
```
    -s, --signoff         add a Signed-off-by trailer
```
option. 

**Think of the sign-off as authorizing others to use your work under the license.** As you might know, authorisation without authentication is fragile, to say the least, hence it is recommended to have authors also digitally sign their work.

### Actual Signatures
Ich you want to digitally sign your work instead of just adding some text comment (recommended), you may *additionally* use
```
    -S, --gpg-sign[=<key-id>]
                          GPG sign commit
```
which can be enabled globally by
```
git config --global user.signingkey [key-id]
```
see https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work .

**Think of the digital signature as authenticating you as the authors.**


### What if we forgot?
In the container shipping team, we did not sign-off our commits in the beginning. But, since a sign off message is not a digital signature, any one who can force push to the main branch can change commit messages in hindsight. Legally, you should obviously make sure that the authors at least agree. [This script](./git-filter-add-signoff.py) is useful to batch add such sign off messages to all commits of certain user(s).

## COC
You should include a [Code of Conduct](https://wiki.hyperledger.org/community/hyperledger-project-code-of-conduct) to explicitly state a few things which might be taken for granted but are better stated explicitly anyway.

