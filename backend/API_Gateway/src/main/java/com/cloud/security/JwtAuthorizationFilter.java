package com.cloud.security;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.filter.OncePerRequestFilter;

import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.interfaces.DecodedJWT;

public class JwtAuthorizationFilter extends OncePerRequestFilter {

	private final JwtProperties jwt;

	public JwtAuthorizationFilter(JwtProperties jwt) {
		this.jwt = jwt;
	}

	@Override
	protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
			throws ServletException, IOException {
		String header = request.getHeader(jwt.getHeader());
		if (header == null || !header.startsWith(jwt.getTokenPrefix())) {
			filterChain.doFilter(request, response);
			return;
		}

		try {
			DecodedJWT verifier = JWT.require(Algorithm.HMAC512(jwt.getSecret().getBytes())).build()
					.verify(header.replace(jwt.getTokenPrefix(), ""));
			String username = verifier.getSubject();
			String[] role = verifier.getClaims().get("role").asArray(String.class);
			List<GrantedAuthority> authority = new ArrayList<>();
			for(int i=0; i<role.length; i++) {
				authority.add(new SimpleGrantedAuthority(role[i]));
			}
			UsernamePasswordAuthenticationToken auth = new UsernamePasswordAuthenticationToken(username, null, authority);
			SecurityContextHolder.getContext().setAuthentication(auth);
		} catch (Exception e) {
			SecurityContextHolder.clearContext();
		}
		filterChain.doFilter(request, response);
	}

}
