package com.cloud.security;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.security.core.AuthenticationException;
import org.springframework.security.web.AuthenticationEntryPoint;
import org.springframework.stereotype.Component;

import com.google.gson.Gson;


@Component
public class UserAuthenticationEntryPoint implements AuthenticationEntryPoint {

	@Override
	public void commence(HttpServletRequest request, HttpServletResponse response,
			AuthenticationException authException) throws IOException, ServletException {
		response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
		response.setContentType("application/json;charset=utf-8");
		Gson gson = new Gson();
		String json = "{'status' : '401', 'message' : '아이디나 비밀번호가 일치하지 않습니다'}";
		
		response.getWriter().print(gson.toJson(json));
	}
}
