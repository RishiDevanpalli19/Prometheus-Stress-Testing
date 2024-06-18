
# **🎯Python Stress/Load Testing using Prometheus and Grafana**

The repository features Prometheus, a stress/load testing tool that generates high loads and monitors its performance using Grafana. When the load exceeds a threshold, an alert is triggered, and metrics are saved in a JSON file, with insights provided via email and WhatsApp notification using Gemini API.


## ⚙️***Technologies Used***

[**-Prometheus:**](https://prometheus.io/) An open-source systems monitoring and alerting toolkit.\
[**-Alertmanager:**](https://prometheus.io/docs/alerting/latest/alertmanager/) Handles alerts sent by Prometheus server.\
[**-Node Exporter:**](https://prometheus.io/docs/guides/node-exporter/) Exports system and hardware metrics.\
[**-Git:**](https://git-scm.com/) Version control system for tracking changes in source code.\
[**-Python3:**](https://www.python.org/) Programming language used for scripting.\
**-JSON:** Data interchange format used for configuration files.\
[**-hPing3:**](https://www.kali.org/tools/hping3/) A command-line oriented TCP/IP packet assembler/analyzer.\
[**-epel-release:**](https://docs.fedoraproject.org/en-US/epel/ometheus.io/) Extra Packages for Enterprise Linux (EPEL) repository release package.\
[**-Gemini API:**](https://ai.google.dev/) Offers robust data analytics and machine learning capabilities for efficient processing and interpretation of large datasets.





## 💥***Getting Started***

To deploy this project run:\
**Step 1**: Shell Script to start all Server/Nodes

```bash
  ./shell_script.sh
```
First, ensure that the script has execute permissions. You can set the permissions using `chmod`
```bash
  chmod +x shell_script.sh
```

**Step 2**: Run `menu.py` to set up the Prometheus stress testing environment:
```bash
  python3 menu.py
```
After the initial setup, goto `<your_ip>:9090` to access Prometheus Server. Here you can view and manage the Alerts.

**Step3**: Running the Flask App\
After the setup is complete, you can run the application using the following command:
```bash
  python3 app.py
```
**Note**: You can set the IP address of your Node Exporter in the `app.py` file. Currently, the option to specify the IP address of the machine running the script is available because stress testing must be performed on the same machine.

**Note**: To receive WhatsApp notifications, create an account in [**Twilio**](https://www.twilio.com/en-us/messaging/channels/whatsapp)  and add the necessary numbers for insights and recommendations from Gemini API.
## ⚠️***Warning***

This stress testing tool performs actions that may damage your computer or your Prometheus setup. Use it with caution.


## 🙌🏻***Contributing***

If you'd like to contribute to this project, please fork the repository and submit a pull request. You can also open an issue to report bugs or suggest improvements.


