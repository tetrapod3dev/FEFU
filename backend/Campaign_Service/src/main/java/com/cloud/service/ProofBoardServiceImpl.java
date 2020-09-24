package com.cloud.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cloud.domain.ProofBoardDto;
import com.cloud.mapper.ProofBoardMapper;

@Service
public class ProofBoardServiceImpl implements ProofBoardService{
	
	@Autowired
	private ProofBoardMapper proofMapper;

	@Override
	public List<ProofBoardDto> findAllByProof(int no, boolean flag, int startIndex, int perPageNum) {
		return proofMapper.findAllByProof(no, flag, startIndex, perPageNum);
	}

	@Override
	public int insertProof(ProofBoardDto dto) {
		return proofMapper.insertProof(dto);
	}

	@Override
	public int updateProof(int no) {
		return proofMapper.updateProof(no);
	}
	
	@Override
	public int totalCount(int no, boolean flag) {
		return proofMapper.totalCount(no, flag);
	}
	
	
	@Override
	public int findTodayPassOfficial(int no) {
		int headcount = proofMapper.findHeadcount(no);
		int pass = proofMapper.findTodayPassOfficial(no);
		return (pass / headcount) * 100;
	}
	
	@Override
	public Map<String, Object> findWeekPassOfficial(int no) {
		int headcount = proofMapper.findHeadcount(no);
		Map<String, Object> map = proofMapper.findWeekPassOfficial(no);
		if(map == null) {
			return null;
		}
		for(String key : map.keySet()) {
			int res = ((int)map.get(key) / headcount) * 100;
			map.replace(key, res);
		}
		return map;
	}
}
