package com.cloud;

import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@SpringBootApplication
@EnableEurekaServer
public class DiscoveryApplication {

	public static void main(String[] args) {
//		SpringApplication.run(DiscoveryApplication.class, args);
		new SpringApplicationBuilder(DiscoveryApplication.class).web(WebApplicationType.SERVLET).run(args);
	}

}
