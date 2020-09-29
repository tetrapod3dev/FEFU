package com.cloud.service;

import com.cloud.domain.UserDto;

public interface UserService {
	
	public UserDto findByUsername(String username);
	public int userRegistier(UserDto dto);
	public int checkByUsername(String usernmae);
	public int checkByNickname(String nickname);
	public int insertUserRole(String usernmae);
}
