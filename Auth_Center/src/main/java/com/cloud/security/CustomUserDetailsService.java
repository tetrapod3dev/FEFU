package com.cloud.security;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.cloud.domain.UserDto;
import com.cloud.mapper.UserMapper;


@Service
public class CustomUserDetailsService implements UserDetailsService{ 
	
	@Autowired
	private UserMapper userMapper;
	
	@Override
	public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
		UserDto user = userMapper.findByUsername(username);
		if(user == null) {
			throw new UsernameNotFoundException("유저 아이디 업음");
		}
		CustomUserDetails principal = new CustomUserDetails(user);
		return principal;
	}

	
}
