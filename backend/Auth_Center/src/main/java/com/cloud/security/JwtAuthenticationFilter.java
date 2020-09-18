package com.cloud.security;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.security.authentication.AuthenticationCredentialsNotFoundException;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.cloud.domain.UserDto;
import com.fasterxml.jackson.databind.ObjectMapper;

public class JwtAuthenticationFilter extends UsernamePasswordAuthenticationFilter {

	private AuthenticationManager authenticationManager;
	private final JwtProperties jwtProperties;

	public JwtAuthenticationFilter(AuthenticationManager authenticationManager, JwtProperties jwtProperties) {
		this.authenticationManager = authenticationManager;
		this.jwtProperties = jwtProperties;
	}
	
	@Override
	public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response)
			throws AuthenticationException {
		UserDto credentials = null;
		try {
			credentials = new ObjectMapper().readValue(request.getInputStream(), UserDto.class);
		} catch(Exception e) {
			logger.error("유저 없음");
		}
		
		UsernamePasswordAuthenticationToken token = new UsernamePasswordAuthenticationToken(
				credentials.getUsername(),
				credentials.getPassword(),
				new ArrayList<>()
			);
		Authentication authRequest = authenticationManager.authenticate(token);
		return authRequest;
	}
	
	@Override
	protected void successfulAuthentication(HttpServletRequest request, HttpServletResponse response, FilterChain chain,
			Authentication authResult) throws IOException, ServletException {
		CustomUserDetails principal = (CustomUserDetails)authResult.getPrincipal();
		
		Iterator<? extends GrantedAuthority> iter = principal.getAuthorities().iterator();
		String[] role = new String[principal.getAuthorities().size()];
		int idx = 0;
		while(iter.hasNext()) {
			role[idx++] = iter.next().getAuthority();
		}
		String token = JWT.create().withSubject(principal.getUsername())
				.withArrayClaim("role", role)
				.withExpiresAt(new Date(System.currentTimeMillis() + jwtProperties.getExpirationTime()))
				.sign(Algorithm.HMAC512(jwtProperties.getSecret().getBytes()));

		logger.info(jwtProperties.getHeader() + " " + jwtProperties.getTokenPrefix() + token);
		response.addHeader(jwtProperties.getHeader(), jwtProperties.getTokenPrefix() + token);
	}

}
