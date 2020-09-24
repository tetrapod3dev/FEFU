package com.cloud.mapper;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.annotations.Mapper;

import com.cloud.domain.ProofBoardDto;

@Mapper
public interface ProofBoardMapper {
	
	public List<ProofBoardDto> findAllByProof(int no, boolean flag, int startIndex, int perPageNum);
	public int totalCount(int no, boolean flag);
	public int insertProof(ProofBoardDto dto);
	public int updateProof(int no);
	public int findHeadcount(int no);
	public int findTodayPassOfficial(int no);
	public Map<String, Object> findWeekPassOfficial(int no);
}
