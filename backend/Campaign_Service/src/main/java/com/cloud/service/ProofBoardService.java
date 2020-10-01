package com.cloud.service;

import java.util.List;
import java.util.Map;

import com.cloud.domain.ProofBoardDto;

public interface ProofBoardService {

	public List<ProofBoardDto> findAllByProof(int no, boolean flag, int startIndex, int perPageNum);
	public int totalCount(int no, boolean flag);
	public int insertProof(ProofBoardDto dto);
	public int updateProof(int no);
	public double findTodayPassOfficial(int no);
	public List<Map<String, Object>> findWeekPassOfficial(int no);
	public double findUserPassPersonal(int no, String username);
	public List<Map<String, Object>> findAllPassPersonal(int no);
}
