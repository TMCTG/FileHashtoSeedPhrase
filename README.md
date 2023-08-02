# FileHashtoSeedPhrase
Utility to derive a seed phrase from the hash of a file, with an optional passphrase check to see the private key and wallet address of the first derived Ethereum address.

This could be used as an alternate way of backing up your seed phrase. If the seed phrase is originally generated in way that is repeatable to produce identical seed phrases.
This proof of concept uses the hash of a file, but any text string could also suffice. Obviously make sure that the file will not change so the file hash will not change, the file is stored securely and backed up, then you could use any innocuous-looking file on your computer/internet/both as input to hash and output as a cryptocurrency seed phrase with an optional passphrase to make it more secure again.

Strongly suggest doing this on an airgapped device if you'll be using the generated seed phrase for storing real funds.


![image](https://github.com/TMCTG/FileHashtoSeedPhrase/assets/93534190/6d6d7e40-846d-4222-b0eb-d5447d0c41a9)
