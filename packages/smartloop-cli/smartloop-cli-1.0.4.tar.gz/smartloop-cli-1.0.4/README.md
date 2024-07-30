# Smartloop Command Line Interface

Smartloop CLI to upload, managed and chat with documents fine-tuned using foundational LLM models. It uses the smartloop API to manage projects and documents and gives you the power to quickly process contents using LLM and reason based on them

## Requirements

- Python 3.11

## Getting Started

Install the CLI with the following command:

```
pip install -U smartloop-cli

```
Once installed, check that everything is setup correclty:


```
$ smartloop-cli --help

 Usage: main.py [OPTIONS] COMMAND [ARGS]...

│ login     Login using a token from https://api.smartloop.ai/v1/redoc                                                                                                            │
│ project                                                                                                                                                                         │
│ run       Starts a chat session with a selected project                                                                                                                         │
│ upload    Upload documents for a slected project                                                                                                                                │
│ whoami    Find out which account you are logged in


```

## Creating Account

First create an account using the `curl` command below, in Linux / macOS / WSL 2.0 / Ubuntu:


```
curl --location --request PUT 'https://api.smartloop.ai/v1/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "email": "<string>",
  "password": "<string>",
  "name": "<string>"
}'

```

You will receive an email with the `token` that is needed to login into the CLI.

## Setting up the CLI

Login to the CLI in the follwoing way using the token recevied in email:

```
smartloop-cli login
```

This command will prompt you for your token, copy and pase the token that you have recevied in your email

```
$ python main.py login
                       _    _
 ___ _ __   __ _  _ _ | |_ | | ___  ___  _ __
(_-<| '  \ / _` || '_||  _|| |/ _ \/ _ \| '_ \ _
/__/|_|_|_|\__,_||_|   \__||_|\___/\___/| .__/(_)
                                        |_|

You can generatate your token from /users/token endpoint
Enter your token (Token will be invisitble):

```


Next step it to create a  project, you can do so with the following command:

```
smartloop-cli project create --name Lexic
```

## Upload Document

Once the project is created , upload documents from your folder or a specific file, in this case I am uploading the a document describing Microsoft online services form my local machine

```
smartloop-cli upload --path=~/OnlineSvcsConsolidatedSLA\(WW\)\(English\)\(June2024\)\(CR\).docx
```

## Run It

Finally, once the document is uploaded and processed, run the CLI to query:

```
smartloop-cli run
```

This will bring up the following interface:

```
$ smartloop-cli run
Current project: Microsoft(microsoft-24-07-2024)
Enter message (Ctrl-C to exit): what the SLA for azure open ai
⠋
The SLA (Service Level Agreement) for Azure OpenAI is not explicitly mentioned in the provided text. However, it's possible that the SLA for Azure OpenAI might be similar to the one mentioned below:

"Uptime Percentage"

* Service Credit:
+ < 99.9%: 10%
+ < 99%: 25%
+ < 95%: 100%

Please note that this is not a direct quote from the provided text, but rather an inference based on the format and structure of the SLA mentioned for other Azure services (e.g., SAP HANA on Azure High Availability Pair). To confirm the actual SLA for Azure OpenAI, you should check the official Microsoft documentation or contact their support team.

Enter message (Ctrl-C to exit):
```


In order to switch a default project, use the following command:

```
smartloop-cli project select 
```


## Contributing

Contributions are welcome! Please create a pull request with your changes. 


## Contact

If you have any questions or suggestions, please feel free to reach out to hello@smartloop.ai


## References

* [Smartloop API Documentation](https://api.smartloop.ai/v1/redoc)

