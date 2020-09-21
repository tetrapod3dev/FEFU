package com.cloud.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import com.cloud.domain.CampaignDto;

@Mapper
public interface CampaignMapper {

	public List<CampaignDto> findAll(String campaignType, int pageNo, String type, String content, int startIndex, int perPageNum);
	public int findByCount(String campaignType, int pageNo, String type, String content);
	public List<String> findTagByNo(int no);
	public CampaignDto findDetail(int no);
	public int insertCampaign(CampaignDto dto);
	public int insertTag(List<String> tag, @Param("no") int no);
	public int updateCampaign(CampaignDto dto);
	public int deleteCampaign(int no);
}
