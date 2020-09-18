package com.cloud.config;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.cloud.netflix.zuul.filters.RouteLocator;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

import springfox.documentation.spi.DocumentationType;
import springfox.documentation.swagger.web.SwaggerResource;
import springfox.documentation.swagger.web.SwaggerResourcesProvider;

@Component
@Primary
@EnableAutoConfiguration
public class CustomSwaggerResourcesProvider implements SwaggerResourcesProvider {

	private final RouteLocator routeLocator;

	public CustomSwaggerResourcesProvider(RouteLocator routeLocator) {
        this.routeLocator = routeLocator;
    }

	@Override
	public List get() {
		List<SwaggerResource> resources = routeLocator.getRoutes().stream().distinct().map(route -> {
			SwaggerResource swaggerResource = new SwaggerResource();
			swaggerResource.setName(route.getLocation());
			swaggerResource.setLocation(route.getFullPath().replace("**", "v2/api-docs"));
			swaggerResource.setSwaggerVersion(DocumentationType.SWAGGER_2.getVersion());

			return swaggerResource;

		}).collect(Collectors.toList());

		return resources;
	}
	/*
	 * @Autowired private ZuulProperties properties;
	 * 
	 * @Override public List<SwaggerResource> get() { List<SwaggerResource>
	 * resources = new ArrayList<SwaggerResource>();
	 * properties.getRoutes().values().stream() .forEach(route ->
	 * resources.add(createResource(route.getServiceId(), route.getLocation())));
	 * return resources; }
	 * 
	 * private SwaggerResource createResource(String name, String location) {
	 * SwaggerResource res = new SwaggerResource(); res.setName(name);
	 * res.setLocation("/" + location); res.setSwaggerVersion("2.0"); return res; }
	 */
}
