import py_eureka_client.eureka_client as eureka_client

eureka_client.init(eureka_server="http://localhost:8761/eureka",
                                                app_name="product-service",
                                                instance_port=8000)
