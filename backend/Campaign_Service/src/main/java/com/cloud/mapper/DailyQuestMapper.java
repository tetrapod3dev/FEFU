package com.cloud.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.cloud.domain.DailyQuestDto;

@Mapper
public interface DailyQuestMapper {

	public List<DailyQuestDto> findAll();
	public List<DailyQuestDto> findByCompleteList(String username);
	public int insertComplete(String username, int no);
}
