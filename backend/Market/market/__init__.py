import py_eureka_client.eureka_client as eureka_client

eureka_client.init(eureka_server="http://j3a402.p.ssafy.io:8761/eureka",
                                                app_name="products",
                                                instance_port=8000)
