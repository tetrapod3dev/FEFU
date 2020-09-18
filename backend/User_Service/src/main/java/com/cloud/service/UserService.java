package com.cloud.service;

import com.cloud.domain.UserDto;

public interface UserService {
	
	public int userRegistier(UserDto dto);
	public int checkByUsername(String usernmae);
	public int insertUserRole(String usernmae);
}
