package com.cloud.security;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import com.cloud.domain.UserDto;

public class CustomUserDetails implements UserDetails {

	private static final long serialVersionUID = 1L;
	private UserDto user;

	public CustomUserDetails(UserDto user) {
		this.user = user;
	}

	@Override
	public Collection<? extends GrantedAuthority> getAuthorities() {
		List<GrantedAuthority> authority = new ArrayList<>();
		for (int i = 0; i < user.getAuth().size(); i++) {
			authority.add(new SimpleGrantedAuthority(user.getAuth().get(i)));
		}
//		authority.add(new SimpleGrantedAuthority("USER_ROLE"));
		return authority;
	}

	@Override
	public String getPassword() {
		return user.getPassword();
	}

	@Override
	public String getUsername() {
		return user.getUsername();
	}

	@Override
	public boolean isAccountNonExpired() {
		return true;
	}

	@Override
	public boolean isAccountNonLocked() {
		return true;
	}

	@Override
	public boolean isCredentialsNonExpired() {
		return true;
	}

	@Override
	public boolean isEnabled() {
		return true;
	}

}
