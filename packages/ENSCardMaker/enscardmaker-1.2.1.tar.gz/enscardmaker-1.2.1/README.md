# ENS Card Maker
This is a Python script that takes an ENS name or ETH address, collects information from https://enstate.rs, and generates an image based on information from an ENS profile.

# Web Version
There's a web version of this tool that can be used by going to `https://enscards.littlebitstudios.com/[user]` where `[user]` is the ENS name or ETH address you want to generate a card for.
The code for this version of the script is hosted at https://github.com/littlebitstudios/ENSCardMakerWeb.

# Usage
The command is:
```
enscardmaker <user> [output]
```
Where `<user>` is the ENS name or ETH address you want to generate a card for, and `[output]` is the file path you want to save the card to. If `[output]` is not provided, the card will be saved to `[user].png`.

# Credits/Licensing
ENS, the brand, is held by ENS Labs Limited.

This software uses the font Inter by Rasmus Andersson, which is licensed under the [SIL Open Font License](https://openfontlicense.org/), a copy of which is at the root of the repository as `LICENSE-Inter.txt`.<br>
The font has a GitHub repository at https://github.com/rsms/inter. The font's creator does not recommend downloading the font from Google Fonts since that version is outdated. You can find the files for this font in this repo's releases.<br>
You can also download the font from the creator's website at https://rsms.me/inter.

As with most of my code, this code is published under the MIT License.
