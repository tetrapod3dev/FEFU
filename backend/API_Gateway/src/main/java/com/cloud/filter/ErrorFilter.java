package com.cloud.filter;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.netflix.zuul.ZuulFilter;
import com.netflix.zuul.context.RequestContext;
import com.netflix.zuul.exception.ZuulException;

public class ErrorFilter extends ZuulFilter {

	private static final Logger logger = LoggerFactory.getLogger(ErrorFilter.class);

	@Override
	public boolean shouldFilter() {
		return true;
	}

	@Override
	public String filterType() {
		return "error";
	}
	
	@Override
	public int filterOrder() {
		return -1;
	}
	
	@Override
	public Object run() throws ZuulException {
		final RequestContext ctx = RequestContext.getCurrentContext();
		final Object e = ctx.get("throwable");
		
		if(e instanceof ZuulException) {
			final ZuulException zuul = (ZuulException)e;
			logger.error("Zuul failure detected: " + zuul.getMessage());
			ctx.remove("throwable");
			ctx.setResponseBody("Overriding Zuul Excetpion Body");
			ctx.getResponse().setContentType("application/json");
			ctx.setResponseStatusCode(503);
		}
		return null;
	}


}
