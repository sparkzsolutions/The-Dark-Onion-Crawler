
---

<p align="center"> Simple app for scrapping data from gumtree.
    <br> 
</p>



## 🧐 About <a name = "about"></a>

The project was created for learning purposes to know how to combine scrapy framework with TorIp changer.
## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites

- Docker desktop

### Project structure
```
.
├── docker-compose.yml
├── LICENSE
├── README.md
└── src
    ├── crawler
    │   ├── __init__.py
    │   ├── items.py
    │   ├── middlewares.py
    │   ├── pipelines.py
    │   ├── settings.py
    │   └── spiders
    │       ├── __init__.py
    │       ├── mieszkania2.py
    │       └── quotes_spider.py
    ├── Dockerfile
    ├── go_spider.py
    ├── scrapy.cfg
    └── tests
        └── ipchanger_works.py
```

### Installing
Clone repository:

```
git clone https://github.com/Santhin/TorScrapy.git
```


To run the crawler type:

```
docker-compose up
```



## 🔧 Running the tests <a name = "tests"></a>

Simple check if tor ip changer is working unmark commented test in dockerfile. <br />
The exemplary output:


<p align="center">
  <a href="" rel="noopener">
 <img src="https://i.imgur.com/eoAwcw7.png" alt="Project logo"></a>
</p>

## 🛠️ Todo

- add control startup for TorIpChanger container in docker-compose


## ⛏️ Built Using <a name = "built_using"></a>

- [Scrapy](https://scrapy.org/) - Crawler
- [TorIpChanger](https://github.com/DusanMadar/TorIpChanger) - Privoxy + Tor


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to DusanMadar for amazing framework and tutorial step by step
https://github.com/DusanMadar/TorIpChanger
https://gist.github.com/DusanMadar/8d11026b7ce0bce6a67f7dd87b999f6b