package com.cloud.mapper;

import org.apache.ibatis.annotations.Mapper;

import com.cloud.domain.UserDto;

@Mapper
public interface UserMapper {
	public int userRegistier(UserDto dto);
	public int checkByUsername(String usernmae);
	public int checkByNickname(String nickname);
	public int insertUserRole(String usernmae);
}
